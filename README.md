# Overview
This project performs security analysis of encryption in Simplified-DES using a white box model, Generalized Additive Model (GAM).This program performs specific analysis by measuring Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and Partial Dependence.

# Description
・This program divides plaintext (8 bits) and S-DES encrypted text (8 bits) into 4 bits each, and uses them as features in GAM. Also, set the key to the target variable.
・Three division methods are set for feature values ​​to compare differences.
　①1 to 4 bits and 5 to 8 bits from the left end
　②1,3,5,7 bits and 2,4,6,8 bits from the left end
　③1,2,5,6 bits and 3,4,7,8 bits from the left end
・Measure MAE, RMSE, and Partial Dependence from the feature values ​​and objective variable values, and compare the respective patterns.

# Requirements
使用したソフトウェア名称、ソフトウェアバージョン等のプログラムの動作環境を書く。

# Install/Usage
プログラムのインストール法や使い方を書く。

# Author
自分の名前を書く。

# References
プログラム作成に参考にした書籍、論文を書く。

# License
掲載しているプログラムのライセンスを書く。
