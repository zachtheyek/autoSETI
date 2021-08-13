import numpy as np
import torch

def generate_local_masks(chunk_size: int,
                         attention_size: int,
                         mask_future=False,
                         device: torch.device = 'cpu') -> torch.BoolTensor:
    """
    Compute attention mask as attention_size wide diagonal.
    Parameters
    ----------
    chunk_size:
        Time dimension size.
    attention_size:
        Number of backward elements to apply attention.
    device:
        torch device. Default is ``'cpu'``.
    Returns
    -------
        Mask as a boolean tensor.
    """
    local_map = np.empty((chunk_size, chunk_size))
    i, j = np.indices(local_map.shape)

    if mask_future:
        local_map[i, j] = (i - j > attention_size) ^ (j - i > 0)
    else:
        local_map[i, j] = np.abs(i - j) > attention_size

    return torch.BoolTensor(local_map).to(device)