% This is a simple MATLAB scrips
% 1 - 5

for i = 1:5
    square = i ^ 2;
    fprintf('The %d square is %d\n', i, square);
end

a = 5;
b = 2;
result = a ^ 2 + b ^ 2;
disp(['result is ', num2str(result)]);
