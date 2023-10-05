## Backend

### Initial Setup of Django

1. Make sure python and pip are installed on the system.
    ```sh
    python --version
    pip --version
    ```

2. Build a dedicated virtual environment for the Django project.
   ```sh
   python -m venv env
   ```

3. Activate the virutal environment(everytime when opening the project).
    ```sh
    source env/bin/activate
    ```

4. Install `DJango` inside this virtual environment.
   ```sh
   python -m pip install Django
   ```
   Check the django verion with
   ```sh
   django-admin --version
   ```

5. Install other dependencies - 
   - `Django REST framework`: It is a powerful and flexible toolkit for building Web APIs, also used for **Authentication** policies like OAuth1a and OAuth2, **Serialization** that supports both ORM and non-ORM data sources, regular function based views, etc.
        ```sh
        pip install djangorestframework
        ``` 
   - `Django-cors-headers`: Adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins
        ```sh
        pip install django-cors-headers
        ``` 
Both can be installed together with
```sh
python -m pip install djangorestframework django-cors-headers
```

<hr>

## Frontend = React + TypeScript + Vite

```
bun create vite@latest frontend
```

React working in Vite with HMR and some ESLint rules.
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) using [SWC](https://swc.rs/) for Fast Refresh