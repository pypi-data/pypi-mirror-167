'''
This custom config file is where you can create output anchors, customize your runtime settings, customize
your runtime information, and register custom fields. 
'''

# pylint: disable=line-too-long
# pylint: disable=too-many-branches
# pylint: disable=pointless-string-statement
# pylint: disable=unused-argument
# pylint: disable=self-assigning-variable
# pylint: disable=invalid-name
# pylint: disable=unused-import

import sys
import datetime
import io
import inspect
import base64
import typing
from typing import List, Dict, Any, Tuple

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# ========================================================
# Artemis Imports
# ========================================================
from artemis_labs.artemis_helper import ArtemisHelper, ArtemisType
from artemis_labs.artemis_config_manager import ArtemisConfigManager
from artemis_labs.artemis_runtime_manager import ArtemisRuntimeManager

# ========================================================
# Run Information and Fields
# ========================================================
run_information = {
    'Test' : 'ABC'
}
ArtemisRuntimeManager.register_run_information(run_information)

fields = {
    'custom' : '123ABC',
}
ArtemisRuntimeManager.register_fields(fields)

runtime_settings = {
    'delay' : 0
}
ArtemisRuntimeManager.register_runtime_settings(runtime_settings)


# ========================================================
# Custom Anchors
# ========================================================
def line_graph_abc(arr , named_args_dict : Dict) -> Tuple:
    '''
    This takes in three arrays of numerical values through named arguments
    data-x, data-y, and data-z, and it uses these arrays to create a 3D surface plot.
    It also takes in named arguments title, x-label, y-label, and z-label, and it uses
    these to customize the graph.

    :param arr: None
    :param named_args_dict: Named arguments provided when invoking decorator
    :return: Serialized surface graph
    '''

    # Unpack
    x = named_args_dict['data-x']
    y = named_args_dict['data-y']
    z = named_args_dict['data-z']

    # Convert type to numpy arrays if lists
    x = ArtemisHelper.convert_if(x, ArtemisType.LIST, ArtemisType.NUMPY_ARRAY)
    y = ArtemisHelper.convert_if(y, ArtemisType.LIST, ArtemisType.NUMPY_ARRAY)
    z = ArtemisHelper.convert_if(z, ArtemisType.LIST, ArtemisType.NUMPY_ARRAY)

    # Plot args
    # setup_plot_args(named_args_dict)

    ax = plt.axes(projection='3d')
    ax.plot_trisurf(x, y, z, cmap='viridis', linewidth=0.1)

    # Serialize plot
    serialized_plot = ArtemisHelper.serialize(None, ArtemisType.MATPLOTLIB_PLOT, named_args_dict)

    # Close figure
    plt.close()

    # Return serialized plot
    return serialized_plot
ArtemisConfigManager.register_function(line_graph_abc, 'line_graph_abc')

