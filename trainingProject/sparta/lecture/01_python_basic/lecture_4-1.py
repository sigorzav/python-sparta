dir(list)

from abc import ABC, abstractmethod

# 먼저 추상 클래스를 만들려면 import로 abc 모듈을 가져와야 한다( abc는 abstract base class의 약자). 
# 그리고 클래스의 ( )(괄호) 안에 metaclass=ABCMeta를 지정하고, 
# 메서드를 만들 때 위에 @abstractmethod를 붙여서 추상 메서드로 지정한다.

# import torch.nn as nn

# PyTorch
# nn.Module