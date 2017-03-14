#!/usr/bin/env bash
cd ~/tensorflow

python3 tensorflow/examples/image_retraining/retrain.py \
--bottleneck_dir=/home/rgio/FGIC/midcars/bottlenecks \
--how_many_training_steps 10000 \
--model_dir=/home/rgio/FGIC/midcars/inception \
--output_graph=/home/rgio/FGIC/midcars/retrained_graph.pb \
--output_labels=/home/rgio/FGIC/midcars/retrained_labels.txt \
--learning_rate=0.003 \
--image_dir /home/rgio/FGIC/midcars/car_photos
