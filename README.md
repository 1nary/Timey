## **timey 🎓web 履修管理アプリ**

***

#### **機能仕様**

- ログイン／ログアウトの認証
- 履修の作成、編集、削除
-

#### **プラットフォーム**

- データベース：SQLite
- フレームワーク：Django
- フロント：HTML
- バックエンド：Python

### **テーブル**

#### **users テーブル**

| カラム       |       型 | 備考 |
| :----------- | -------: | :--: |
| id           |  integer |  -   |
| nickname     |  varchar |  -   |
| email        |  varchar |  -   |
| password     |  varchar |  -   |
| last_login   | datetime |  -   |
| is_superuser |     bool |  -   |
| is_active    |     bool |  -   |

#### lectures テーブル

| カラム  |      型 |    備考    |
| :------ | ------: | :--------: |
| id      | integer |     -      |
| name    | varchar |     -      |
| teacher | varchar |     -      |
| room    | varchar |     -      |
| week    | integer |     -      |
| period  | integer |     -      |
| user_id | integer | ForeignKey |

***
<br>

![twitter-card](https://user-images.githubusercontent.com/114323587/219702369-65a4cb68-93b1-4546-9141-ae40dbb4c958.png)
