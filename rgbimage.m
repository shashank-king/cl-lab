% Read image and separate color channels
x = imread("/home/rguktrkvalley/Pictures/redcolor.png");
red = x(:,:,1);  % Extract red channel
gr = x(:,:,2);  % Extract green channel
bl = x(:,:,3);  % Extract blue channel

% Save channels to CSV files
csvwrite("red.csv", red);
csvwrite("gr.csv", gr);
csvwrite("bl.csv", bl);
