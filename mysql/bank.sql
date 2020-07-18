/*==============================================================*/
/* DBMS name:      Sybase SQL Anywhere 16                       */
/* Created on:     2020/5/4 11:47:14                            */
/*==============================================================*/
create database bank;

use bank;

/*==============================================================*/
/* Table: account                                               */
/*==============================================================*/


create table account 
(
   account_type         int                            null,
   account_number       char(30)                       not null,
   brance               float                          null,
   sub_bank_name        varchar(50)                    null,
   start_date           date                           null,
   rate                 float                          null,
   currency_type        int                            null,
   overdraft            float                          null,
   constraint PK_ACCOUNT primary key (account_number)
);

/*==============================================================*/
/* Index: account_PK                                            */
/*==============================================================*/
create unique index account_PK on account (
account_number ASC
);

/*==============================================================*/
/* Table: apply                                                 */
/*==============================================================*/
create table apply 
(
   loan_id              varchar(60)                    not null,
   id_number            char(30)                       not null,
   constraint PK_APPLY primary key clustered (loan_id, id_number)
);

/*==============================================================*/
/* Index: apply_PK                                              */
/*==============================================================*/
create unique  index apply_PK on apply (
loan_id ASC,
id_number ASC
);

/*==============================================================*/
/* Index: apply_FK                                              */
/*==============================================================*/
create index apply_FK on apply (
loan_id ASC
);

/*==============================================================*/
/* Index: apply_FK2                                             */
/*==============================================================*/
create index apply_FK2 on apply (
id_number ASC
);

/*==============================================================*/
/* Table: client                                                */
/*==============================================================*/
create table client 
(
   id_number            char(30)                       not null,
   sta_id_number        char(30)                       null,
   name                 varchar(15)                    null,
   phonenumber          char(20)                       null,
   addr                 varchar(30)                    null,
   contact_name         varchar(20)                    null,
   contact_phonenumber  char(20)                       null,
   contact_email        varchar(30)                    null,
   contact_relationship varchar(12)                    null,
   constraint PK_CLIENT primary key (id_number)
);

/*==============================================================*/
/* Index: client_PK                                             */
/*==============================================================*/
create unique index client_PK on client (
id_number ASC
);

/*==============================================================*/
/* Index: charge_FK                                             */
/*==============================================================*/
create index charge_FK on client (
sta_id_number ASC
);



/*==============================================================*/
/* Table: department                                            */
/*==============================================================*/
create table department 
(
   department_id        varchar(20)                    not null,
   name                 varchar(50)                    null,
   department_name      varchar(20)                    null,
   department_type      int                            null,
   depart_manager_id    char(30)                       null,
   constraint PK_DEPARTMENT primary key (department_id)
);

/*==============================================================*/
/* Index: department_PK                                         */
/*==============================================================*/
create unique index department_PK on department (
department_id ASC
);

/*==============================================================*/
/* Index: belong_FK                                             */
/*==============================================================*/
create index belong_FK on department (
name ASC
);

/*==============================================================*/
/* Table: loans                                                 */
/*==============================================================*/
create table loans 
(
   loan_id              varchar(60)                    not null,
   name                 varchar(50)                    null,
   amount               float                          null,
   amount_payed         float                          null,
   constraint PK_LOANS primary key (loan_id)
);

/*==============================================================*/
/* Index: loans_PK                                              */
/*==============================================================*/
create unique index loans_PK on loans (
loan_id ASC
);

/*==============================================================*/
/* Index: provide_FK                                            */
/*==============================================================*/
create index provide_FK on loans (
name ASC
);

/*==============================================================*/
/* Table: own                                                   */
/*==============================================================*/
create table own 
(
   id_number            char(30)                       not null,
   account_number       char(30)                       not null,
   last_date            date                           null,
   constraint PK_OWN primary key clustered (id_number, account_number)
);

/*==============================================================*/
/* Index: own_PK                                                */
/*==============================================================*/
create unique  index own_PK on own (
id_number ASC,
account_number ASC
);

/*==============================================================*/
/* Index: own_FK                                                */
/*==============================================================*/
create index own_FK on own (
id_number ASC
);

/*==============================================================*/
/* Index: own_FK2                                               */
/*==============================================================*/
create index own_FK2 on own (
account_number ASC
);

/*==============================================================*/
/* Table: pay                                                   */
/*==============================================================*/
create table pay 
(
   pay_id               varchar(60)                    not null,
   name                 varchar(50)                    null,
   loan_id              varchar(60)                    null,
   pay_amount           float                          null,
   constraint PK_PAY primary key (pay_id)
);

/*==============================================================*/
/* Index: pay_PK                                                */
/*==============================================================*/
create unique index pay_PK on pay (
pay_id ASC
);

/*==============================================================*/
/* Index: pay_FK                                                */
/*==============================================================*/
create index pay_FK on pay (
name ASC
);

/*==============================================================*/
/* Table: staff                                                 */
/*==============================================================*/
create table staff 
(
   id_number            char(30)                       not null,
   dep_department_id    varchar(20)                    null,
   dep_id_number        char(30)                       null,
   name                 varchar(15)                    null,
   phonenumber          char(20)                       null,
   addr                 varchar(30)                    null,
   date_start           date                           null,
   constraint PK_STAFF primary key (id_number)
);

/*==============================================================*/
/* Index: staff_PK                                              */
/*==============================================================*/
create unique index staff_PK on staff (
id_number ASC
);

/*==============================================================*/
/* Index: belong_FK                                             */
/*==============================================================*/
create index belong_FK on staff (
dep_department_id ASC
);

/*==============================================================*/
/* Index: lead_FK                                               */
/*==============================================================*/
create index lead_FK on staff (
dep_id_number ASC
);

/*==============================================================*/
/* Table: sub_branch                                            */
/*==============================================================*/
create table sub_branch 
(
   name                 varchar(50)                    not null,
   asset                float                          null,
   city                 char(20)                       null,
   constraint PK_SUB_BRANCH primary key (name)
);

/*==============================================================*/
/* Index: sub_branch_PK                                         */
/*==============================================================*/
create unique index sub_branch_PK on sub_branch (
name ASC
);

alter table account
   add constraint FK_ACCOUNT_REFERENCE_SUB_BRAN foreign key (sub_bank_name)
      references sub_branch (name)
      on update restrict
      on delete restrict;


alter table apply
   add constraint FK_APPLY_APPLY_CLIENT foreign key (id_number)
      references client (id_number)
      on update restrict
      on delete restrict;

alter table apply
   add constraint FK_APPLY_APPLY_LOANS foreign key (loan_id)
      references loans (loan_id)
      on update restrict
      on delete restrict;

alter table client
   add constraint FK_CLIENT_CHARGE_STAFF foreign key (sta_id_number)
      references staff (id_number)
      on update restrict
      on delete restrict;




alter table department
   add constraint FK_DEPARTME_BELONG_SUB_BRAN foreign key (name)
      references sub_branch (name)
      on update restrict
      on delete restrict;


alter table loans
   add constraint FK_LOANS_PROVIDE_SUB_BRAN foreign key (name)
      references sub_branch (name)
      on update restrict
      on delete restrict;

alter table own
   add constraint FK_OWN_OWN_ACCOUNT foreign key (account_number)
      references account (account_number)
      on update restrict
      on delete restrict;

alter table own
   add constraint FK_OWN_OWN_CLIENT foreign key (id_number)
      references client (id_number)
      on update restrict
      on delete restrict;

alter table pay
   add constraint FK_PAY_REFERENCE_LOANS foreign key (loan_id)
      references loans (loan_id)
      on update restrict
      on delete restrict;

alter table pay
   add constraint FK_PAY_PAY_SUB_BRAN foreign key (name)
      references sub_branch (name)
      on update restrict
      on delete restrict;

alter table staff
   add constraint FK_STAFF_BELONG_DEPARTME foreign key (dep_department_id)
      references department (department_id)
      on update restrict
      on delete restrict;


alter table staff add password char(30) not NULL;

insert into sub_branch 
value
('USTC建设银行', 1000000.10,'合肥'),
('江西省吉安市建设银行', 1000000.10,'吉安');

INSERT INTO department 
value
('001', 'USTC建设银行', '业务部', 1, '362421199911232012'),
('011', '江西省吉安市建设银行', '业务部', 1, '362421199911232013');

INSERT INTO staff 
value
('362421199911232012','001','362421199911232012','cs1033','17755554433','USTC','2019-02-08','1033');
INSERT INTO staff 
value
('1','001','362421199911232012','刘同学','17755554433','USTC','2019-02-08','1033');
INSERT INTO staff 
value
('362421199911232013','011','362421199911232013','LGC','17755554433','USTC','2019-02-08','1033');
INSERT INTO staff 
value
('2','011','362421199911232013','刘高聪','17755554433','USTC','2019-02-08','1033');

ALTER TABLE pay ADD pay_date date;
ALTER TABLE loans ADD loan_date date;


