{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Preprocess",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNlBhUVMEmFXx2bbaPSpk9q",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/10-Academy-Batch-4-Week-4/Swahili-Speech-To-Text/blob/main/Preprocess.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4zlBa10DS9TO"
      },
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5aUSpRwcPwrK"
      },
      "source": [
        "#load packages\n",
        "import json\n",
        "import os\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import string\n",
        "import matplotlib.pyplot as plt\n",
        "%matplotlib inline\n",
        "import librosa\n",
        "import librosa.display\n",
        "import IPython.display as  ipd\n",
        "import torch\n",
        "import torchaudio\n",
        "from torchaudio import transforms"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aGoTcxuHS0Wo"
      },
      "source": [
        "os.chdir(\"drive/My Drive/train\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "G6s_mNRLS_r3"
      },
      "source": [
        "DATASET_PATH = \"wav\"\n",
        "SAMPLE_RATE = 22050\n",
        "labels=[]\n",
        "def preprocess(dataset_path):\n",
        "    # dictionary to store files\n",
        "    \n",
        "    # loop through all sub-folders\n",
        "    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):\n",
        "\n",
        "        # ensure we're processing at sub-folder level\n",
        "        if dirpath is not dataset_path:\n",
        "\n",
        "            # save label (i.e., sub-folder name) in the mapping eg SWH-05-20101106\n",
        "            label = dirpath.split(\"/\")[-1]\n",
        "           \n",
        "            print(\"\\nProcessing: {}\".format(label))\n",
        "\n",
        "            # process all audio files in genre sub-dir\n",
        "            for f in filenames:\n",
        "\n",
        "\t\t        # load audio file\n",
        "                filename=\"wav/\"+label+\"/\"+f\n",
        "                labels.append(filename)\n",
        "                 \n",
        "if __name__ == \"__main__\":\n",
        "    preprocess(DATASET_PATH)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xw4OxH-eTFUW"
      },
      "source": [
        "df=pd.read_csv(\"text.txt\",sep=\"\\t\",header=None)\n",
        "df = df.drop([0],axis=1)\n",
        "df.columns=['text']\n",
        "df['audio']=labels"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WEf2xuDeXSmQ"
      },
      "source": [
        "def clean_column(data:pd.DataFrame,col:str):\n",
        "  words_list=[' UNK ', ' music ', ' laughter ']\n",
        "  data = data[~data[col].isin(words_list)]\n",
        "  for row in data[col]:\n",
        "    for punctuation in string.punctuation:\n",
        "        row = row.replace(punctuation,\" \")\n",
        "    return row\n",
        "  return data"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}