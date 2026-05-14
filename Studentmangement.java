public class StudentManagementSystem {

    // Student class
    public class Student {

        public String name;
        public Integer age;
        public String grade;

        // Constructor
        public Student(String name, Integer age, String grade) {
            this.name = name;
            this.age = age;
            this.grade = grade;
        }
    }

    // Method to display students
    public static void displayStudents() {

        // Create list of students
        List<Student> students = new List<Student>();

        // Add students
        students.add(new Student('Rohit', 20, 'A'));
        students.add(new Student('Raj', 21, 'B'));
        students.add(new Student('Priyansh', 19, 'A'));

        // Display student details
        for (Student s : students) {

            System.debug('Name: ' + s.name);
            System.debug('Age: ' + s.age);
            System.debug('Grade: ' + s.grade);
            System.debug('----------------------');
        }
    }
}