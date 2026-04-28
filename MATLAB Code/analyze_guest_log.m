% Reading the data from the txt file
data = readtable('guest_log.txt');

% Extracting columns from the data
roommates = data.Roommate;
actions = data.Action;
guests = data.Guests;

% Graph 1: Total Guests Added per Roommate
r1_added = sum(strcmp(roommates, 'Roommate 1') & strcmp(actions, 'Added Guest'));
r2_added = sum(strcmp(roommates, 'Roommate 2') & strcmp(actions, 'Added Guest'));
r3_added = sum(strcmp(roommates, 'Roommate 3') & strcmp(actions, 'Added Guest'));

figure(1); clf;
x = 1:3;
vals = [r1_added, r2_added, r3_added];

hold on;
bar(x(1), vals(1), 'm');
bar(x(2), vals(2), 'g');
bar(x(3), vals(3), 'b');
hold off;

xticks(x);
xticklabels({'Roommate 1', 'Roommate 2', 'Roommate 3'});
ylabel('Number of Guests Added');
title('Total Guests Added per Roommate');
grid on;


% Graph 2: Number of Sessions per Roommate
% A session = one "Selected" action
r1_sessions = sum(strcmp(roommates, 'Roommate 1') & strcmp(actions, 'Selected'));
r2_sessions = sum(strcmp(roommates, 'Roommate 2') & strcmp(actions, 'Selected'));
r3_sessions = sum(strcmp(roommates, 'Roommate 3') & strcmp(actions, 'Selected'));

figure(2); clf;
vals = [r1_sessions, r2_sessions, r3_sessions];

hold on;
bar(x(1), vals(1), 'm');
bar(x(2), vals(2), 'g');
bar(x(3), vals(3), 'b');
hold off;

xticks(x);
xticklabels({'Roommate 1', 'Roommate 2', 'Roommate 3'});
ylabel('Number of Sessions');
title('Number of Sessions per Roommate');
grid on;


% Graph 3: Max Guests Reached per Roommate
r1_max = sum(strcmp(roommates, 'Roommate 1') & strcmp(actions, 'Denied - Max Guests'));
r2_max = sum(strcmp(roommates, 'Roommate 2') & strcmp(actions, 'Denied - Max Guests'));
r3_max = sum(strcmp(roommates, 'Roommate 3') & strcmp(actions, 'Denied - Max Guests'));

figure(3); clf;
vals = [r1_max, r2_max, r3_max];

hold on;
bar(x(1), vals(1), 'm');
bar(x(2), vals(2), 'g');
bar(x(3), vals(3), 'b');
hold off;

xticks(x);
xticklabels({'Roommate 1', 'Roommate 2', 'Roommate 3'});
ylabel('Times Denied (Max Guests)');
title('Times Each Roommate Hit the Guest Limit');
grid on;


% Graph 4: Guest Count Over Time for Each Roommate
timeVals = data.TimePassed;

r1_idx = strcmp(data.Roommate, 'Roommate 1');
r2_idx = strcmp(data.Roommate, 'Roommate 2');
r3_idx = strcmp(data.Roommate, 'Roommate 3');

figure(4); clf;
hold on;

plot(timeVals(r1_idx), data.Guests(r1_idx), 'm-o', 'LineWidth', 1.5);
plot(timeVals(r2_idx), data.Guests(r2_idx), 'g-o', 'LineWidth', 1.5);
plot(timeVals(r3_idx), data.Guests(r3_idx), 'b-o', 'LineWidth', 1.5);

hold off;

xlabel('Time Passed (hh:mm:ss)');
ylabel('Guest Count');
title('Guest Count Over Time for Each Roommate');
legend({'Roommate 1', 'Roommate 2', 'Roommate 3'}, 'Location', 'northwest');
grid on;
