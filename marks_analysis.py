#include <stdio.h>

int main() {
    int n;
    printf("Enter number of students: ");
    scanf("%d", &n);

    char name[50][20];
    int math[50], science[50], english[50], computer[50], social[50];
    int total[50];
    float percentage[50];
    char result[50][5];
    char grade[50][3];

    // -------- INPUT PHASE --------
    for(int i = 0; i < n; i++) {
        printf("\nEnter details of student %d\n", i+1);

        printf("Name: ");
        scanf("%s", name[i]);

        printf("Math marks: ");
        scanf("%d", &math[i]);

        printf("Science marks: ");
        scanf("%d", &science[i]);

        printf("English marks: ");
        scanf("%d", &english[i]);

        printf("Computer marks: ");
        scanf("%d", &computer[i]);

        printf("Social marks: ");
        scanf("%d", &social[i]);

        total[i] = math[i] + science[i] + english[i] + computer[i] + social[i];
        percentage[i] = total[i] / 5.0;

        // Pass / Fail & Grade
        if(math[i] < 35 || science[i] < 35 || english[i] < 35 ||
           computer[i] < 35 || social[i] < 35) {
            sprintf(result[i], "Fail");
            sprintf(grade[i], "F");
        } else {
            sprintf(result[i], "Pass");
            if(percentage[i] >= 90)
                sprintf(grade[i], "A+");
            else if(percentage[i] >= 80)
                sprintf(grade[i], "A");
            else if(percentage[i] >= 70)
                sprintf(grade[i], "B");
            else if(percentage[i] >= 60)
                sprintf(grade[i], "C");
            else
                sprintf(grade[i], "D");
        }
    }

    // -------- OUTPUT PHASE --------
    printf("\n========== STUDENT RESULTS ==========\n");

    for(int i = 0; i < n; i++) {
        printf("\nStudent %d Result\n", i+1);
        printf("------------------\n");
        printf("Name       : %s\n", name[i]);
        printf("Math       : %d\n", math[i]);
        printf("Science    : %d\n", science[i]);
        printf("English    : %d\n", english[i]);
        printf("Computer   : %d\n", computer[i]);
        printf("Social     : %d\n", social[i]);
        printf("Total      : %d\n", total[i]);
        printf("Percentage : %.2f\n", percentage[i]);
        printf("Result     : %s\n", result[i]);
        printf("Grade      : %s\n", grade[i]);
    }

    return 0;
}
