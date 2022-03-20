FROM fusuf/asenauserbot:latest
RUN git clone https://github.com/sahibziko/delta /root/Userator
WORKDIR /root/Userator/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
