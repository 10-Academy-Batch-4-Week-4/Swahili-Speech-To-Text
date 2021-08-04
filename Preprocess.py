{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Preprocess",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMnLeHX5dAmIlk5GR1q3OBT",
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
        "<a href=\"https://colab.research.google.com/github/katenjoki/Swahili-Speech-To-Text/blob/main/Preprocess.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5aUSpRwcPwrK",
        "outputId": "9f1faa54-4ca3-4c8a-a331-a08d93a3c257"
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
        "from torchaudio import transforms\n",
        "\n",
        "from google.colab import drive\n",
        "drive.mount('/content/drive')\n",
        "\n",
        "os.chdir(\"drive/My Drive/train\")\n",
        "\n",
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
        "    preprocess(DATASET_PATH)\n",
        "\n",
        "df=pd.read_csv(\"text.txt\",sep=\"\\t\",header=None)\n",
        "df = df.drop([0],axis=1)\n",
        "df.columns=['text']\n",
        "df['audio']=labels\n",
        "\n"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n",
            "\n",
            "Processing: SWH-05-20101106\n",
            "\n",
            "Processing: SWH-05-20101107\n",
            "\n",
            "Processing: SWH-05-20101109\n",
            "\n",
            "Processing: SWH-05-20101110\n",
            "\n",
            "Processing: SWH-05-20101111\n",
            "\n",
            "Processing: SWH-05-20101112\n",
            "\n",
            "Processing: SWH-05-20101113\n",
            "\n",
            "Processing: SWH-05-20101121\n",
            "\n",
            "Processing: SWH-05-20101123\n",
            "\n",
            "Processing: SWH-05-20110114\n",
            "\n",
            "Processing: SWH-05-20110123\n",
            "\n",
            "Processing: SWH-05-20110125\n",
            "\n",
            "Processing: SWH-05-20110215\n",
            "\n",
            "Processing: SWH-05-20110317\n",
            "\n",
            "Processing: SWH-05-20110321\n",
            "\n",
            "Processing: SWH-05-20110327\n",
            "\n",
            "Processing: SWH-15-20101103\n",
            "\n",
            "Processing: SWH-15-20101104\n",
            "\n",
            "Processing: SWH-15-20101109\n",
            "\n",
            "Processing: SWH-15-20101113\n",
            "\n",
            "Processing: SWH-15-20101115\n",
            "\n",
            "Processing: SWH-15-20101117\n",
            "\n",
            "Processing: SWH-15-20101130\n",
            "\n",
            "Processing: SWH-15-20101227\n",
            "\n",
            "Processing: SWH-15-20110124\n",
            "\n",
            "Processing: SWH-15-20110126\n",
            "\n",
            "Processing: SWH-15-20110207\n",
            "\n",
            "Processing: SWH-15-20110224\n",
            "\n",
            "Processing: SWH-15-20110303\n",
            "\n",
            "Processing: SWH-15-20110310\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}