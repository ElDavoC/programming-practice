#include <stdio.h>
#include <stdlib.h>
#define MAX_STRING_LENGTH 6

// DEFAULT CODE ******************

struct package
{
	char* id;
	int weight;
};

typedef struct package package;

struct post_office
{
	int min_weight;
	int max_weight;
	package* packages;
	int packages_count;
};

typedef struct post_office post_office;

struct town
{
	char* name;
	post_office* offices;
	int offices_count;
};

typedef struct town town;

//**************************


// SOLUTION **********************************

int stringCompare(char* a, char* b) {
    while(*a != '\0' && *b != '\0') {
        if(*a != *b){
            return 0;
        }

        if(*a != '\0'){
            a++;
        }

        if(*b != '\0'){
            b++;
        }
    }
    return 1;
}

void print_all_packages(town t) {
    printf("%s:\n", t.name);
    for(int i = 0; i < t.offices_count; i++) {
        printf("\t%d:\n", i);
        for(int j = 0; j < t.offices[i].packages_count; j++) {
            printf("\t\t%s\n", t.offices[i].packages[j].id);
        }
    }
}

void send_all_acceptable_packages(town* source, int source_office_index, town* target, int target_office_index) {
    int min_weight = target->offices[target_office_index].min_weight;
    int max_weight = target->offices[target_office_index].max_weight;
    int i = 0;
    int package_weight;

    while(i < source->offices[source_office_index].packages_count) {
        package_weight = source->offices[source_office_index].packages[i].weight;
        if(package_weight >= min_weight && package_weight <= max_weight) {
            int final_packages_count = ++target->offices[target_office_index].packages_count;
            target->offices[target_office_index].packages = realloc(target->offices[target_office_index].packages, sizeof(package) * final_packages_count);
            target->offices[target_office_index].packages[final_packages_count-1] = source->offices[source_office_index].packages[i];
            for(int j = i; j < source->offices[source_office_index].packages_count - 1; j++) {
                source->offices[source_office_index].packages[j] = source->offices[source_office_index].packages[j + 1];
            }
            final_packages_count = --source->offices[source_office_index].packages_count;
            source->offices[source_office_index].packages = realloc(source->offices[source_office_index].packages, sizeof(package) * final_packages_count);
            i--;
        }
        i++;
    }
}

town town_with_most_packages(town* towns, int towns_count) {
    int max_packages = 0;
    int the_town = 0;
    int total;

    for(int i = 0; i < towns_count; i++) {
        total = 0;
        for(int j = 0; j < towns[i].offices_count; j++) {
            total += towns[i].offices[j].packages_count;
        }
        if(total > max_packages) {
            max_packages = total;
            the_town = i;
        }
    }
    return towns[the_town];
}

town* find_town(town* towns, int towns_count, char* name) {
    for(int i = 0; i < towns_count; i++) {
        if(stringCompare(towns[i].name, name)) {
            return &towns[i];
        }
    }
}
// *******************************


// DEFAULT CODE ***********************************


int main()
{
	int towns_count;
	printf("Insert number of towns: ");
	scanf("%d", &towns_count);
	town* towns = malloc(sizeof(town)*towns_count);
	for (int i = 0; i < towns_count; i++) {
		towns[i].name = malloc(sizeof(char) * MAX_STRING_LENGTH);
		printf("Town %d name: ", i);
		scanf("%s", towns[i].name);
		printf("Offices count: ");
		scanf("%d", &towns[i].offices_count);
		towns[i].offices = malloc(sizeof(post_office)*towns[i].offices_count);
		for (int j = 0; j < towns[i].offices_count; j++) {
            printf("\tOffice %d parameters: ", j);
			scanf("%d%d%d", &towns[i].offices[j].packages_count, &towns[i].offices[j].min_weight, &towns[i].offices[j].max_weight);
			towns[i].offices[j].packages = malloc(sizeof(package)*towns[i].offices[j].packages_count);
			for (int k = 0; k < towns[i].offices[j].packages_count; k++) {
				towns[i].offices[j].packages[k].id = malloc(sizeof(char) * MAX_STRING_LENGTH);
                printf("\t\tPackage %d id: ", k);
				scanf("%s", towns[i].offices[j].packages[k].id);
				printf("\t\tPackage %d weight: ", k);
				scanf("%d", &towns[i].offices[j].packages[k].weight);
			}
		}
	}
	int queries;
	printf("Number of queries: ");
	scanf("%d", &queries);
	char town_name[MAX_STRING_LENGTH];
	while (queries--) {
		int type;
		printf("Type of query: ");
		scanf("%d", &type);
		getchar();
		switch (type) {
		case 1:
		    printf("\tTown name: ");
			scanf("%s", town_name);
			town* t = find_town(towns, towns_count, town_name);
			print_all_packages(*t);
			break;
		case 2:
		    printf("\tTown name(source): ");
			scanf("%s", town_name);
			town* source = find_town(towns, towns_count, town_name);
			int source_index;
			printf("\tSource index: ");
			scanf("%d", &source_index);
			printf("\tTown name(target): ");
			scanf("%s", town_name);
			town* target = find_town(towns, towns_count, town_name);
			int target_index;
			printf("\tTarget index: ");
			scanf("%d", &target_index);
			send_all_acceptable_packages(source, source_index, target, target_index);
			break;
		case 3:
			printf("Town with the most number of packages is %s\n", town_with_most_packages(towns, towns_count).name);
			break;
		}
	}
	for (int i = 0; i < towns_count; i++) {
        for (int j = 0; j < towns[i].offices_count; j++) {
            for (int k = 0; k < towns[i].offices[j].packages_count; k++) {
                free(towns[i].offices[j].packages[k].id);
            }
            free(towns[i].offices[j].packages);
        }
        free(towns[i].offices);
        free(towns[i].name);
    }
    free(towns);
	return 0;
}
