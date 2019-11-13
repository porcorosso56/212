FROM postgres:12.0
EXPOSE 5432

# Prerequisites
RUN apt update
RUN apt install -y build-essential curl git python3
RUN adduser --disabled-password --gecos "" user

# Homebrew setup
RUN echo | su - user -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"
RUN su - user -c "echo 'eval $(/home/user/.linuxbrew/bin/brew shellenv)' >>~/.profile"
RUN echo 'eval $(/home/user/.linuxbrew/bin/brew shellenv)' >>~/.profile

# Postgres setup
COPY init.sh /docker-entrypoint-initdb.d/

# In the sake of demo
RUN su - user -c "brew install cowsay"

COPY dumper.py /usr/bin/dumper
COPY greet.py /usr/bin/greet

CMD /docker-entrypoint-initdb.d/init.sh && clear && greet; bash --login
