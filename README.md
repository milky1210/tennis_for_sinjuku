# tennis_for_sinjuku
新宿区用のテニスコート監視・予約コード
## 環境整備
pip3 install hogehoge

にてパッケージを収集する。

selenium, chrome-driver をhogehogeに代入すると良い。

pythonやそのパッケージは読者の環境次第なので、お好みの方法で必要なライブラリ、ドライバをインストールしてほしい。

## ユーザー情報ファイルに情報書き入れ
sample_pwd_id.jsonファイルに新宿区の団体IDとパスワードを入力し、ファイル名をpwd_id.jsonに変更することで利用できます。

##ビルド方法

python observe.py

にて監視用コードを動かし、平日19:00-と土日祝日のコートが空いた時にとる
