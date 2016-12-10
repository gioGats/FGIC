#!/usr/bin/env bash
cd ~/tensorflow

python3 tensorflow/examples/image_retraining/retrain.py \
--bottleneck_dir=/home/rgio/FGIC/cars/bottlenecks \
--how_many_training_steps 20000 \
--model_dir=/home/rgio/FGIC/cars/inception \
--output_graph=/home/rgio/FGIC/cars/retrained_graph.pb \
--output_labels=/home/rgio/FGIC/cars/retrained_labels.txt \
--image_dir /home/rgio/FGIC/cars/car_photos
