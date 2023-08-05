# -*- coding: utf-8 -*-
# ! /usr/bin/env python
""" `SyntheticDataset` allows to return a generative model as torch dataset. """

from torch.utils.data import Dataset


class SyntheticDataset(Dataset):
    """A synthetic dataset containing data generated by a model of medigan

    Parameters
    ----------
    samples: list
        List of data points in the dataset e.g. generated images as numpy array.
    masks: list
        List of segmentation masks, if applicable,  pertaining to the `samples` items
    other_imaging_output: list
        List of other imaging output produced by the generative model (e.g. specific types of other masks/modalities)
    labels: list
        list of labels, if applicable, pertaining to the `samples` items
    transform:
        torch compose transform functions that are applied to the torch dataset.

    Attributes
    ----------
    samples: list
        List of data points in the dataset e.g. generated images as numpy array.
    masks: list
        List of segmentation masks, if applicable,  pertaining to the `samples` items
    other_imaging_output: list
        List of other imaging output produced by the generative model (e.g. specific types of other masks/modalities)
    labels: list
        list of labels, if applicable, pertaining to the `samples` items
    transform:
        torch compose transform functions that are applied to the torch dataset.
    """

    def __init__(
        self,
        samples,
        masks=None,
        other_imaging_output=None,
        labels=None,
        transform=None,
    ):
        self.samples = samples
        self.masks = masks
        self.other_imaging_output = other_imaging_output
        self.labels = labels
        self.transform = transform

    def __getitem__(self, index):
        x = self.samples[index]
        y = self.labels[index] if self.labels is not None else None
        mask = self.masks[index] if self.masks is not None else None
        other_imaging_output = (
            self.other_imaging_output[index]
            if self.other_imaging_output is not None
            else None
        )

        if self.transform:
            if mask is not None:
                if other_imaging_output is not None:
                    x, mask, other_imaging_output = self.transform(
                        x, mask, other_imaging_output
                    )
                # transform needs to be applied to both mask and image.
                x, mask = self.transform(x, mask)
            elif other_imaging_output is not None:
                x, other_imaging_output = self.transform(x, other_imaging_output)
            else:
                x = self.transform(x)
        item = {"sample": x}  # extendable dictionary
        if y is not None:
            item["label"] = y
        if mask is not None:
            item["mask"] = mask
        if other_imaging_output is not None:
            item["other_imaging_output"] = other_imaging_output
        return item

    def __len__(self):
        return len(self.samples)
