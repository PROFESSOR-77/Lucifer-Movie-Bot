if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/PROFESSOR-77/Lucifer-Movie-Bot.git /LuciferMovie-Bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Lucifer-Movie-Bot
fi
cd /Lucifer-Movie-Bot
pip3 install -U -r requirements.txt
echo "Starting Lucifer Movie Bot...."
python3 main.py
