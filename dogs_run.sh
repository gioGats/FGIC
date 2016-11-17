cd ~/tensorflow

python3 tensorflow/examples/image_retraining/retrain.py \
--bottleneck_dir=/home/rgio/FGIC/dogs/bottlenecks \
--model_dir=/home/rgio/FGIC/dogs/inception \
--output_graph=/home/rgio/FGIC/dogs/retrained_graph.pb \
--output_labels=/home/rgio/FGIC/dogs/retrained_labels.txt \
--image_dir /home/rgio/FGIC/dogs/dog_photos
