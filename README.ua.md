## Injective Python SDK

### Залежності

**Ubuntu**
```bash
sudo apt install python3.X-dev autoconf automake build-essential libffi-dev libtool pkg-config
```
**Fedora**
```bash
sudo dnf install python3-devel autoconf automake gcc gcc-c++ libffi-devel libtool make pkgconfig
```

**macOS**

```bash
brew install autoconf automake libtool
```

### Швидкий старт
Установка
```bash
pip install injective-py
```

### Використання
Вимагає Python 3.7+

[Приклади](https://github.com/InjectiveLabs/sdk-python/tree/master/examples)
```bash
$ pipenv shell
$ pipenv install

# Підключення до API біржі Injective
# та прослуховування нових ордерів на певному ринку
$ python examples/exchange_client/spot_exchange_rpc/8_StreamOrders.py

# Відправка повідомлення з банківським переказом
# підписує і відправляє транзакцію в Injective Chain
$ python examples/chain_client/1_MsgSend.py
```
Оновіть `pip` до останньої версії, якщо ви бачите ці попередження:
  ```
 WARNING: Value for scheme.platlib does not match. Please report this to <https://github.com/pypa/pip/issues/10151>
 WARNING: Additional context:   user = True   home = None   root = None   prefix = None
  ```

### Розробка
1. Генерація прото-binding та збірка
  ```
  make gen
  python -m build
  ```

2. Активація середовища розробки
  ```
  pipenv shell
  pipenv install --dev
  ```

3. Встановлення пакету
  ```
  # з локальної збірки
  pip uninstall injective-py
  pip install injective-py --no-index --find-links /path/to/injective/sdk-python/dist

  # з pypi
  pip uninstall injective-py
  pip install injective-py
  ```

4. Отримання останньої конфігурації denom
```
python pyinjective/fetch_metadata.py
```

Зверніть увагу, що [синхронний клієнт](https://github.com/InjectiveLabs/sdk-python/blob/master/pyinjective/client.py) був відмічений як застарілий з 18 квітня 2022 року. Якщо ви використовуєте синхронний клієнт, будь ласка, переконайтеся, що перейшли на [асинхронний клієнт](https://github.com/InjectiveLabs/sdk-python/blob/master/pyinjective/async_client.py), Докладнішу інформацію читайте [тут](https://github.com/InjectiveLabs/sdk-python/issues/101)

5. Встановіть середовище розробки (потрібно `pipenv`)
```
pipenv install -d
```

6. Запустіть всі модульні тести у середовищі розробки
```
make tests
```

### Журнал змін
**0.6.5**
* Вилучено `k8s` зі списку підтримуваних вузлів основної мережі (замість нього слід використовувати `lb`

**0.6.4**
* Змінено log-логіку ведення журналу, щоб використовувати окремі логери для кожного модуля та класу.
* Виправлена проблема, яка перешкоджала запитуванню історичних ордерів на ринках spot та derivative для більш ніж одного market_id
* Додано `pytest` як залежність розробки для реалізації та запуску модульних тестів.

**0.6.3.3**
* Оновлено код до нової структури відповідей на транзакцій.

**0.6.3.1**
* Оновлено код до нової структури відповідей симуляції транзакцій.

**0.6.2.7**
* Виправлено обчислення маржі в утилітах.

**0.6.2.1**
* Видалено залежності версій з файлу Pipfile.

**0.6.2.0**
* Додано  MsgUnderwrite та MsgRequestRedemption у Composer

**0.6.1.8**
* Додано MsgCreateInsuranceFund у Composer
* Перегенеровано головні домени мережі.

**0.6.1.5**
* Додано  MsgExecuteContract у Composer

**0.6.1.4**
* Додано wMATIC

**0.6.1.2**
* Додано метод OrderbookV2 у асинхронному клієнті.

**0.6.1.1**
* Додано ARB/USDT

**0.6.0.9**
* Застаріло K8S і встановлено LB як типове значення.
* Перегенеровано прото.

**0.6.0.8**
* Додано USDCfr

**0.6.0.7**
* Додано LDO

**0.6.0.6**
* Встановлено типові значення для кінцевих точок тестової мережі K8S
* Видалено конфігурацію LB для тестової мережі.
* Виправлено відносні імпорти у Composer.
* Додано  AccountPortfolio та StreamAccountPortfolio

**0.6.0.5**
* Додано нові кінцеві точки для тестової мережі.
* Перегенеровано головні домени мережі.

**0.6.0.4**
* Видалено явно вказані версії залежностей protobuf та grpcio-tools.

**0.6.0.2**
* Перегенеровано головні домени мережі.

**0.6.0.0**
* Змінено дефолтну мережу на LB.
* Перегенеровано головні домени мережі.

**0.5.9.7**
* Перегенеровано головні домени мережі.

**0.5.9.6**
* Перегенеровано прото.

**0.5.9.5**
* Додано методи знімка стакана замовлень.

**0.5.9.4**
* Перегенеровано головні домени мережі.

**0.5.9.4**
* Перегенеровано головні домени мережі.

**0.5.9.2**
* Виправлено конвертацію маржі для бінарних опціонів.

**0.5.9.1**
* Додано параметри skip/limit до запиту BinaryOptionsMarketsRequest

**0.5.9.0**
* Перегенеровано прото.
* Виправлено MsgRewardsOptOut
* Видалено залежність від pysha3
  
**0.5.8.8**
* Додано grpc_explorer_endpoint у мережу
* Додано канал та стаб (`explorer channel` та `stub`).

*Зміни, які потребують негайної уваги:*

- Клієнти, які використовують [Custom Network](https://github.com/InjectiveLabs/sdk-python/blob/master/pyinjective/constant.py#L166) тепер повинні встановлювати grpc_explorer_endpoint під час ініціалізації.


## Ліцензія

Авторські права © 2021 - 2022 Injective Labs Inc. (https://injectivelabs.org/)

<a href="https://drive.google.com/uc?export=view&id=1-fPQRh_D_dnun2yTtSsPW5MypVBOVYJP"><img src="https://drive.google.com/uc?export=view&id=1-fPQRh_D_dnun2yTtSsPW5MypVBOVYJP" style="width: 300px; max-width: 100%; height: auto" />

Оригінально видано Injective Labs Inc. under: <br />
Apache License <br />
Версія 2.0, Січень 2004 <br />
http://www.apache.org/licenses/ 
