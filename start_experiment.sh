for i in $(seq 1 5); do
    python main.py easy$i | tee ./logs/easy$i.log;
done

for i in $(seq 1 5); do
    python main.py medium$i | tee ./logs/medium$i.log;
done

for i in $(seq 1 5); do
    python main.py hard$i | tee ./logs/hard$i.log;
done