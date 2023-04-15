#!/usr/bin/env bash
# exit on error
set -o errexit

<<<<<<< HEAD
pip install -r ./electrical/requirements.txt
=======
pip install -r requirements.txt
>>>>>>> 9f9cc44dc4ff56fc553e90d02f0e0fc27dcd4cd6

python manage.py collectstatic --no-input
python manage.py migrate