#!/bin/sh

while true; do
    # Вызов Python скрипта для проверки подключения к БД
    python /usr/src/app/src/check_db_connection.py
    result=$?
    echo "Результат выполнения Python скрипта: $result"
    # Если Python скрипт завершился с кодом 0 (успех), прервать цикл
    if [ $result -eq 0 ]; then
        echo "Успешное подключение к БД."
        break
    else
        echo "Повторная попытка подключиться к БД через 5 секунд..."
    fi

    # Ожидание 5 секунд перед следующей попыткой
    sleep 5
done

set -ex

chmod -R 777 /usr/src/app/var/log
python /usr/src/app/src/manage.py makemigrations --noinput
python /usr/src/app/src/manage.py migrate
python /usr/src/app/src/manage.py collectstatic --noinput --clear

chmod -R 777 media
chmod -R 777 static

exec "$@"

python /usr/src/app/src/manage.py runserver 0.0.0.0:8000
