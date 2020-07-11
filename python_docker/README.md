# BUILD
docker build -t merge_array .

# RUN
docker run merge_array "[1, 2, 3, 3]" "[4, 5, 6]”
