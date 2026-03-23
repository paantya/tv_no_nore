# MTProto Proxy Infrastructure

Инфраструктура для запуска 3-х MTProto прокси (mtg), 1-го SOCKS5 прокси, а также Prometheus и Grafana для мониторинга.

## Быстрый запуск

1.  Скопируйте пример файла переменных окружения:
    ```bash
    cp .env.example .env
    ```

2.  Заполните секреты в файле `.env`:
    *   `MTG_SECRET_1`, `MTG_SECRET_2`, `MTG_SECRET_3` — секреты для MTProto (можно сгенерировать через `head -c 16 /dev/urandom | xxd -ps`).
    *   `SOCKS5_USER`, `SOCKS5_PASSWORD` — логин и пароль для SOCKS5 прокси.
    *   `GRAFANA_ADMIN_USER`, `GRAFANA_ADMIN_PASSWORD` — данные для входа в Grafana.

3.  Сгенерируйте конфигурационные файлы для `mtg`:
    ```bash
    python3 render-configs.py
    ```

4.  Запустите стек:
    ```bash
    docker compose up -d
    ```

## Доступные порты

*   `9443` — MTProto Proxy #1
*   `9444` — MTProto Proxy #2
*   `9445` — MTProto Proxy #3
*   `8443` — SOCKS5 Proxy
*   `9090` — Prometheus
*   `3000` — Grafana

## Мониторинг

Чтобы убедиться, что метрики собираются:
1.  Откройте Prometheus по адресу `http://localhost:9090`.
2.  Перейдите в меню `Status -> Targets`. Все 3 таргета `mtg` должны быть в состоянии `UP`.
3.  Выполните запрос `up{job="mtg"}` в строке поиска Prometheus.
