# -*- coding: utf-8 -*-
"""01_prepare_dataset

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pe-4Jkd85gXyRoMQJT8Ml9low41Vpn3k
"""



# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import datetime
from IPython.display import display
from statsmodels.stats.proportion import proportions_ztest
import matplotlib.pyplot as plt
import seaborn as sns;

# %matplotlib inline

pd.options.display.max_columns = None

from google.colab import drive
drive.mount('/content/drive')

"""# Load experiment Design data

## 1. Load Email list
"""

# hard code Email lists. Email ID is the index of the Email in the list

PO_number_list = ['ml_funding_enables_investing','ml_investing_starts_here','ml_explore_the_app_investing',
                  'ml_funding_faq','ml_user_clustering_emails_fracs','ml_funding_is_safe','ml_picking_an_investment',
                  'ml_investing_101','ml_diversified_portfolio','ml_explore_the_app_list']

"""## 2. Load user segment information"""

segment_group_init_df = pd.read_csv('/content/drive/MyDrive/Email_project/sample_segment_groups.csv')
segment_group_init_df = segment_group_init_df.drop(columns='Unnamed: 0')
segment_group_init_df.head(20)

"""## 3. Load sampled users with Email delivery orders for the experiment"""

sample_exp_df = pd.read_csv('/content/drive/MyDrive/Email_project/sample_uuid_email_order.csv')
sample_exp_df.head()

sample_exp_df.shape

"""# load current user status"""

user_event_df = pd.read_csv('/content/drive/MyDrive/Email_project/user_events.csv')
user_event_df.head()

user_event_df.columns

"""# Load the current status for control groups.

Thay have the same sagmentation rules in the beginning of the experiment.  
These users did not received any Emails during the experiment.
"""

fund_control_df = pd.read_csv('/content/drive/MyDrive/Email_project/control_groups_rate.csv')
fund_control_df.head()