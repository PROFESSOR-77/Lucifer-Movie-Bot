if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/DarkLord-99/LuciferMoringstar-Robot.git /LuciferMoringstar-Robot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /LuciferMoringstar-Robot
fi
cd /LuciferMoringstar-Robot
pip3 install -U -r requirements.txt
echo "Starting Movie Club Bot...."
python3 main.py
