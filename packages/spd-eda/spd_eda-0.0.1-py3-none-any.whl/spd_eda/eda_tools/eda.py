import pandas as pd


# helper functions to process individual variables
def is_numeric_type(s, num_types=['int64', 'float64']):
    if s.dtype in num_types:
        return True
    else:
        return False


def get_distinct_values(s):
    return s.nunique(dropna=False)


def has_missing_values(s):
    if pd.isna(s).sum() > 0:
        return True
    else:
        return False


def create_ordinal_bin_series(s, q=5, missing_bin_label='Missing'):
    qcut_labels = pd.qcut(s, q=q, duplicates='drop').astype(str)
    qcut_labels[qcut_labels == 'nan'] = missing_bin_label
    qcut_labels.name = f"{s.name}_binned"
    return qcut_labels


def create_categorical_bin_series(s, max_categories=100, other_bin_label='Other-Values'):
    stand_alone_categories = list(s.value_counts().sort_values(ascending=False).iloc[:max_categories].index)
    binned_values = s.copy()
    binned_values.name = f"{s.name}_binned"
    binned_values[~binned_values.isin(stand_alone_categories)] = other_bin_label
    return binned_values


def create_categorical_series_no_missing(s, null_replacement='Missing-Values'):
    new_series = s.fillna(null_replacement).copy()
    new_series.name = f"{s.name}_clean"
    return new_series


class DataframeEda:
    def __init__(self, df, agg_fcn, control_var_list=[], ord_bin_threshold=100, ord_bin_count=5, cat_value_limit=30):
        self.df = df
        self.agg_fcn = agg_fcn
        self.control_var_list = control_var_list
        self.ord_bin_threshold = ord_bin_threshold
        self.ord_bin_count = ord_bin_count
        self.cat_value_limit = cat_value_limit

        self.var_summary = self.get_var_summary()
        self.control_df_list = self.get_control_total_summaries()
        self.var_info_dict = self.get_var_info_dict()

    def get_var_summary(self):
        return self.df.describe(include='all').T

    def get_control_total_summaries(self):
        control_df_list = []
        for var in self.control_var_list:
            control_df_list.append(self.df.groupby(var).apply(self.agg_fcn))
        return control_df_list

    def get_var_info_dict(self):
        col_info = {}
        for col in self.df.columns.tolist():
            if is_numeric_type(self.df[col]):
                if get_distinct_values(self.df[col]) > self.ord_bin_threshold:
                    binned_values = create_ordinal_bin_series(self.df[col], q=self.ord_bin_count)
                    col_info[col] = pd.concat([self.df, binned_values], axis=1).groupby(binned_values.name).apply(
                        self.agg_fcn)
                else:
                    col_info[col] = self.df.groupby(col).apply(self.agg_fcn)
            else:
                if get_distinct_values(self.df[col]) > self.cat_value_limit:
                    binned_values = create_categorical_bin_series(self.df[col], max_categories=self.cat_value_limit)
                    col_info[col] = pd.concat([self.df, binned_values], axis=1).groupby(binned_values.name).apply(
                        self.agg_fcn)
                else:
                    cleaned_values = create_categorical_series_no_missing(self.df[col])
                    col_info[col] = pd.concat([self.df, cleaned_values], axis=1).groupby(cleaned_values.name).apply(
                        self.agg_fcn)

        return col_info
