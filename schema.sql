drop table if exists events;
create table events (
       id integer primary key autoincrement,
       title string not null,
       datestamp date not null
);

drop table if exists moments;
create table moments (
       id integer primary key autoincrement,
       title string not null,
       event_id integer references event(id)
);