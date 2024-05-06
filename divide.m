function result = divide_real_numbers(num1, num2)
    if isnumeric(num1) && isnumeric(num2)
        if num2 ~= 0
            result = num1 / num2;
        else
            result = "Error: Cannot divide by zero.";
        end
    else
        result = "Error: Both inputs must be real numbers.";
    end
end

% Take input from the user
number1 = input('Enter the first number: ', 's');
number2 = input('Enter the second number: ', 's');

if ~isnan(str2double(number1)) && ~isnan(str2double(number2))
    result = divide_real_numbers(str2double(number1), str2double(number2));
    disp(['Result of division: ', num2str(result)]);
else
    disp('Error: Please enter valid real numbers.');
end
