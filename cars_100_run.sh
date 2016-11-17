cd ~/tensorflow

python3 tensorflow/examples/image_retraining/retrain.py \
--bottleneck_dir=/home/rgio/FGIC/cars_100/bottlenecks \
--how_many_training_steps 10000 \
--model_dir=/home/rgio/FGIC/cars_100/inception \
--output_graph=/home/rgio/FGIC/cars_100/retrained_graph.pb \
--output_labels=/home/rgio/FGIC/cars_100/retrained_labels.txt \
--learning_rate=0.003 \
--image_dir /home/rgio/FGIC/cars_100/car_photos
