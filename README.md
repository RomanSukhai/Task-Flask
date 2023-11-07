# Task-Flask

## Підготовка та встановлення

1. **Встановлення pyenv**

    - Встановіть `pyenv` відповідно до [інструкцій для вашої ОС](https://github.com/pyenv/pyenv#installation).

2. **Встановлення Python обраної версії (бажано 3.7.0)**

    ```bash
    pyenv install {номер версії відповідно до варіанту}
    pyenv global {номер версії відповідно до варіанту}
    ```


3. **Створення та активація віртуального середовища**

    - Для того щоб знати шлях до скачаної версії python 

   ```bash
    pyenv which python{версія}
   ```

    ```bash
    {шлях до python.exe} -m venv myenv
    source myenv/bin/activate  # на Unix
    .\myenv\Scripts\Activate  # на Windows
    ```

    - Додайте `myenv/` до файлу `.gitignore`, щоб уникнути коміту віртуального середовища до репозиторію:

    ```bash
    echo "myenv/" >> .gitignore
    ```

4. **Встановлення Flask**

    ```bash
    pip install -r requirements.txt
    ```

5. **Реалізація та запуск маршруту**

    В вашому основному файлі Flask (наприклад, `app.py`) додайте:

    ```python
    from flask import Flask
    app = Flask(__name__)

    @app.route('/api/v1/hello-world-{номер варіанту}')
    def hello_world():
        return f"Hello World {номер варіанту}", 200

    if __name__ == '__main__':
        app.run()
    ```

    Запустіть ваш застосування:

    ```bash
    python app.py
    ```

    Перевірте у браузері за адресою:

    ```
    http://localhost:5000/api/v1/hello-world-{номер варіанту}
    ```

6. **Запуск проекту через WSGI сервер**

    Для прикладу використаємо `waitress`:

    ```bash
    waitress-serve --listen=*:8000 app:app
    ```

    **Примітка**: переконайтеся, що `app` - це ім'я вашого модуля, де розташований ваш код Flask.
