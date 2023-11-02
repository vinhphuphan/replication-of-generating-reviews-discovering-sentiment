{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "9b626605",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ae6b0c88",
   "metadata": {},
   "outputs": [],
   "source": [
    "def preprocess_and_split_data(input_file):\n",
    "    # Read the CSV data\n",
    "    df = pd.read_csv(input_file)\n",
    "\n",
    "    # Extract \"reviews.text\" and \"reviews.rating\" columns\n",
    "    df = df[['text', 'stars']]\n",
    "\n",
    "    # Drop rows with missing values\n",
    "    df.dropna(subset=['text', 'stars'], inplace=True)\n",
    "\n",
    "    # Rename the columns to match the desired format\n",
    "    df.rename(columns={'text': 'sentence', 'stars': 'label'}, inplace=True)\n",
    "\n",
    "    # Convert ratings to binary labels\n",
    "    df['label'] = df['label'].apply(lambda x: 1 if x >= 4 else 0)\n",
    "\n",
    "    # Split the data into training, validation, and test sets\n",
    "    train_df, val_df, test_df = np.split(df.sample(frac=1, random_state=42), [int(.7*len(df)), int(.8*len(df))])\n",
    "\n",
    "    # Save the datasets to CSV files\n",
    "    train_df.to_csv(\"yelp_train.csv\", index=False, columns=['label', 'sentence'], header=['label', 'sentence'])\n",
    "    val_df.to_csv(\"yelp_val.csv\", index=False, columns=['label', 'sentence'], header=['label', 'sentence'])\n",
    "    test_df.to_csv(\"yelp_test.csv\", index=False, columns=['label', 'sentence'], header=['label', 'sentence'])\n",
    "\n",
    "# Example usage:\n",
    "input_file = \"yelp.csv\"  # Replace with the actual CSV file path\n",
    "preprocess_and_split_data(input_file)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
