x = [1 2 3 4 5 4 3 2 1];
l = length(x);
y = [];
for i = 1:(l-1)
  diff = x(i+1) - x(i);
  y = [y diff];
end
plot(x);
hold on;
plot(y);
hold off;
