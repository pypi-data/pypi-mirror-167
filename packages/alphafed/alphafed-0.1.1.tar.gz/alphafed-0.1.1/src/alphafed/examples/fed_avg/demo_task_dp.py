"""A differential privacy demo."""

import os
from typing import Any, Dict

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from opacus import PrivacyEngine
from torch.utils.data import DataLoader

from .. import logger
from .fed_avg import DEV_TASK_ID, FedAvgScheduler

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

AGGREGATOR_ID = 'QmegaqF4RjBjN3i4NdJy24svtFkJAUXc3YUFqRKqNjaAw4'
DATA_OWNER_3_ID = 'QmP4DksaGVrFgkNp3d4NxZnnb4RtQucpMqLESJTAEAtuxC'
DATA_OWNER_4_ID = 'QmWuc1GSaqCkUajoPG5QHfeh72YqU4N7VH7Nx2eP6FyJ9M'
DATA_OWNER_5_ID = 'QmRj3kV7uQeCndrJvYYFHwfDoQmFdxNkCqpiL7m7VanKfw'


class DemoScheduler(FedAvgScheduler):

    def __init__(self,
                 min_clients: int,
                 max_clients: int,
                 name: str = None,
                 max_rounds: int = 0,
                 merge_epoch: int = 1,
                 calculation_timeout: int = 300,
                 log_rounds: int = 0,
                 is_centralized: bool = True) -> None:
        super().__init__(min_clients=min_clients,
                         max_clients=max_clients,
                         name=name,
                         max_rounds=max_rounds,
                         merge_epochs=merge_epoch,
                         calculation_timeout=calculation_timeout,
                         log_rounds=log_rounds,
                         is_centralized=is_centralized)
        self.batch_size = 64
        self.learning_rate = 0.01
        self.momentum = 0.5
        self.log_interval = 5
        self.random_seed = 42

        torch.manual_seed(self.random_seed)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        self.model = self.make_model()
        self.optimizer = torch.optim.SGD(self.model.parameters(),
                                         lr=self.learning_rate,
                                         momentum=self.momentum)
        self.train_loader = self.make_train_dataloader()
        # start 差分隐私配置
        self.privacy_engine = PrivacyEngine()
        _model, _optimizer, _data_loader = self.privacy_engine.make_private(
            module=self.model,
            optimizer=self.optimizer,
            data_loader=self.train_loader,
            noise_multiplier=1.1,
            max_grad_norm=1.0,
        )
        self.model = _model
        self.optimizer = _optimizer
        self.train_loader = _data_loader

    def make_model(self) -> nn.Module:
        class ConvNet(nn.Module):
            def __init__(self) -> None:
                super().__init__()
                self.conv1 = nn.Conv2d(in_channels=1, out_channels=10, kernel_size=5)
                self.conv2 = nn.Conv2d(in_channels=10, out_channels=20, kernel_size=5)
                self.conv2_drop = nn.Dropout2d()
                self.fc1 = nn.Linear(in_features=320, out_features=50)
                self.fc2 = nn.Linear(in_features=50, out_features=10)

            def forward(self, x):
                x = F.relu(F.max_pool2d(self.conv1(x), 2))
                x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
                x = x.view(-1, 320)
                x = F.relu(self.fc1(x))
                x = F.dropout(x, training=self.training)
                x = self.fc2(x)
                return F.log_softmax(x, dim=-1)

        return ConvNet()

    def make_train_dataloader(self) -> DataLoader:
        return DataLoader(
            torchvision.datasets.MNIST(
                os.path.join(self.name, 'data'),
                train=True,
                download=True,
                transform=torchvision.transforms.Compose([
                    torchvision.transforms.ToTensor(),
                    torchvision.transforms.Normalize((0.1307,), (0.3081,))
                ])
            ),
            batch_size=self.batch_size,
            shuffle=True
        )

    def make_test_dataloader(self) -> DataLoader:
        return DataLoader(
            torchvision.datasets.MNIST(
                os.path.join(self.name, 'data'),
                train=False,
                download=True,
                transform=torchvision.transforms.Compose([
                    torchvision.transforms.ToTensor(),
                    torchvision.transforms.Normalize((0.1307,), (0.3081,))
                ])
            ),
            batch_size=self.batch_size,
            shuffle=False
        )

    def state_dict(self) -> Dict[str, torch.Tensor]:
        return self.model.state_dict()

    def load_state_dict(self, state_dict: Dict[str, torch.Tensor]):
        self.model.load_state_dict(state_dict)

    def train(self) -> None:
        self.model.train()
        for data, labels in self.train_loader:
            data: torch.Tensor
            labels: torch.Tensor
            data, labels = data.to(self.device), labels.to(self.device)
            self.optimizer.zero_grad()
            output = self.model(data)
            loss = F.nll_loss(output, labels)
            loss.backward()
            self.optimizer.step()

    def test(self):
        self.model.eval()
        test_loss = 0
        correct = 0
        with torch.no_grad():
            test_loader = self.make_test_dataloader()
            for data, labels in test_loader:
                data: torch.Tensor
                labels: torch.Tensor
                data, labels = data.to(self.device), labels.to(self.device)
                output: torch.Tensor = self.model(data)
                test_loss += F.nll_loss(output, labels, reduction='sum').item()
                pred = output.max(1, keepdim=True)[1]
                correct += pred.eq(labels.view_as(pred)).sum().item()

        test_loss /= len(test_loader.dataset)
        correct_rate = 100. * correct / len(test_loader.dataset)
        logger.info(f'Test set: Average loss: {test_loss:.4f}')
        logger.info(
            f'Test set: Accuracy: {correct}/{len(test_loader.dataset)} ({correct_rate:.2f}%)'
        )

    def validate_context(self):
        super().validate_context()
        train_loader = self.make_train_dataloader()
        assert train_loader and len(train_loader) > 0
        test_loader = self.make_train_dataloader()
        assert test_loader and len(test_loader) > 0


def get_task_id() -> str:
    return DEV_TASK_ID


def get_scheduler() -> DemoScheduler:
    return DemoScheduler(min_clients=1,
                         max_clients=2,
                         name='demo_task',
                         max_rounds=5,
                         log_rounds=1,
                         calculation_timeout=120)
