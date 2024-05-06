
filename = "data.csv";
formatSpec = "%s %f %f"; 
[headers, data] = textscan(fopen(filename), formatSpec, "headerlines", 1);
disp(data);
