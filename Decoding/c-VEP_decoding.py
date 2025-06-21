#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jordy Thielen (jordy.thielen@donders.ru.nl)
@modifier: Juliette van Lohuizen (juliette.vanlohuizen@ru.nl)
Changes concerning ICA application and channel removal were made by Juliette.
"""

import os
import numpy as np
import joblib
import mne
import pandas as pd
import pyntbci

# Decide whether to apply ICA or not
ica = True

# Define directories
if ica is True:
    data_dir = '/Users/juliette/Desktop/thesis/preprocessing/c-VEP_preprocessing/c-VEP_ICA'
    save_dir = '/Users/juliette/Desktop/thesis/results/c-VEP/c-VEP_ICA'
else:
    data_dir = '/Users/juliette/Desktop/thesis/preprocessing/c-VEP_preprocessing'
    save_dir = '/Users/juliette/Desktop/thesis/results/c-VEP'

subjects = [
    "VPpdia", "VPpdib", "VPpdic", "VPpdid", "VPpdie", "VPpdif", "VPpdig", "VPpdih", "VPpdii", "VPpdij", "VPpdik",
    "VPpdil", "VPpdim", "VPpdin", "VPpdio", "VPpdip", "VPpdiq", "VPpdir", "VPpdis", "VPpdit", "VPpdiu", "VPpdiv",
    "VPpdiw", "VPpdix", "VPpdiy", "VPpdiz", "VPpdiza", "VPpdizb", "VPpdizc"
]

tasks = ["overt", "covert"]

# Define parameters
event = "dur"
onset_event = True
encoding_length = 0.3
ensemble = True
n_folds = 4

# Define performance arrays
accuracy = np.zeros((len(subjects), len(tasks), n_folds))
accuracy_se = np.zeros((len(subjects), len(tasks)))
accuracy_mean = np.zeros((len(subjects), len(tasks)))

# Loop participants
for i_subject, subject in enumerate(subjects):
    print(f"{subject}", end="\t")

    # Loop tasks
    for i_task, task in enumerate(tasks):
        print(f"{task}: ", end="")

        # Load data
        if ica is True:
            fn = os.path.join(data_dir, f"sub-{subject}_task-{task}_ICA.npz")
        else:
            fn = os.path.join(data_dir, f"sub-{subject}_task-{task}.npz")
        tmp = np.load(fn)
        fs = int(tmp["fs"])
        X = tmp["X"]
        y = tmp["y"]
        V = tmp["V"]

        # Cross-validation
        folds = np.repeat(np.arange(n_folds), int(X.shape[0] / n_folds))
        for i_fold in range(n_folds):
            # Split data to train and test set
            X_trn, y_trn = X[folds != i_fold, :, :], y[folds != i_fold]
            X_tst, y_tst = X[folds == i_fold, :, :], y[folds == i_fold]
            print()

            # Train classifier
            rcca = pyntbci.classifiers.rCCA(stimulus=V, fs=fs, event=event, encoding_length=encoding_length,
                                            onset_event=onset_event, ensemble=ensemble)
            print("Shape of X_trn:", X_trn.shape)
            print("Shape of y_trn:", y_trn.shape)
            rcca.fit(X_trn, y_trn)

            # Apply classifier
            yh_tst = rcca.predict(X_tst)
            print("shape of X_tst:", X_tst.shape)

            # Compute accuracy
            accuracy[i_subject, i_task, i_fold] = np.mean(yh_tst == y_tst)

        # Compute mean and standard error
        fold_accuracies = accuracy[i_subject, i_task, :]
        accuracy_mean[i_subject, i_task] = fold_accuracies.mean()
        accuracy_se[i_subject, i_task] = np.round(fold_accuracies.std() / np.sqrt(n_folds), 2)

        print(f"{accuracy[i_subject, i_task, :].mean():.3f}", end="\t")
    print()

print(f"Average:\tovert: {accuracy[:, 0, :].mean():.3f}\tcovert: {accuracy[:, 1, :].mean():.3f}")

if ica is True:
    np.savez(os.path.join(save_dir, "c-VEP_rcca_ICA.npz"), accuracy=accuracy, accuracy_mean=accuracy_mean, accuracy_se=accuracy_se)
else:
    np.savez(os.path.join(save_dir, "c-VEP_rcca.npz"), accuracy=accuracy, accuracy_mean=accuracy_mean, accuracy_se=accuracy_se)
