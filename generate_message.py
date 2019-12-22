name_input = input("Enter names seperated by comma: ");
ass_input = input("Enter assignment input seperated by comma: ");
grade_input = input("Enter grades input seperated by comma: ");
name_list = list(name_input.split(','));
ass_list= list(ass_input.split(','));
grade_list= list(grade_input.split(','));

for name, ass, grade in zip(name_list,ass_list,grade_list):
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to\
    submit before you can graduate. You're current grade is {} and can increase\
    to {} if you submit all assignments before the due date.\n\n"

    print(message.format(name, ass, grade, int(grade) + int(ass)*2));

