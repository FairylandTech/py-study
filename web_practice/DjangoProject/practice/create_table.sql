create databse if not exit base_info;
DROP TABLE IF EXISTS user_info;
create table user_info(
    id int primary key auto_increment comment 'id',
    name varchar(10) not null comment '姓名',
    account varchar(18) not null comment '账号',
    department varchar(15)  comment '部门',
    status int not null default 1 comment '启用状态',
    create_at timestamp not null default current_timestamp comment'创建时间',
    update_at timestamp not null default current_timestamp on update current_timestamp comment'更新时间'
);

insert into user_info(name,account,department) values ('阿米娅','amy','战斗部');