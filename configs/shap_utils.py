# -*- coding: utf-8 -*-
"""shap_utils.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1beO34pfunJskCmNlDMhiVJWyID6f8tIn
"""

def shap_analysis(net, x, condition, feature_names, save_path_prefix):
    """
    Perform SHAP analysis on the given model and input data,
    then save summary bar plots.

    Args:
        net (torch.nn.Module): Trained PyTorch model that takes (x, condition).
        x (torch.Tensor): Input tensor features (without condition).
        condition (torch.Tensor): Condition tensor (single feature or more).
        feature_names (list of str): List of feature names corresponding to x.

    Returns:
        shap_values: Computed SHAP values.
    """

# Concatenate features and condition along columns
x_combined = torch.cat((x, condition), dim=1)

# Wrapper class so the model receives combined input but forwards separately
class NetWrapper(torch.nn.Module):
    def __init__(self, net):
        super(NetWrapper, self).__init__()
        self.net = net

    def forward(self, x):
        return self.net(x[:, :-1], x[:, -1])

wrapped_net = NetWrapper(net)

# Create SHAP DeepExplainer
explainer = shap.DeepExplainer(wrapped_net, x_combined)
shap_values = explainer.shap_values(x_combined)

# Update feature names by adding 'Condition'
feature_names += ['Condition']

# Generate SHAP summary plots
shap.summary_plot(shap_values, x_combined, plot_type="bar", feature_names=feature_names, max_display=50, show=False)
plt.savefig("/content/drive/MyDrive/jan_files/shap_summary_bar_50.svg")

shap.summary_plot(shap_values, x_combined, plot_type="bar", feature_names=feature_names, max_display=20, show=False)
plt.savefig("/content/drive/MyDrive/jan_files/shap_summary_bar_20.svg")