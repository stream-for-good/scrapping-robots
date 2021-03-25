<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20210324102812 extends AbstractMigration
{
    public function getDescription() : string
    {
        return '';
    }

    public function up(Schema $schema) : void
    {
        // this up() migration is auto-generated, please modify it to your needs
        $this->addSql('CREATE TABLE data (id INT AUTO_INCREMENT NOT NULL, task_id INT NOT NULL, log LONGTEXT NOT NULL, INDEX IDX_ADF3F3638DB60186 (task_id), PRIMARY KEY(id)) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');
        $this->addSql('CREATE TABLE robot (id INT AUTO_INCREMENT NOT NULL, `label` VARCHAR(255) NOT NULL, category VARCHAR(255) NOT NULL, PRIMARY KEY(id)) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');
        $this->addSql('CREATE TABLE `task` (id INT AUTO_INCREMENT NOT NULL, robot_id INT NOT NULL, `state` VARCHAR(255) NOT NULL, `loop` VARCHAR(255) NOT NULL, date DATETIME NOT NULL, INDEX IDX_527EDB25D5AA10AC (robot_id), PRIMARY KEY(id)) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');
        $this->addSql('ALTER TABLE data ADD CONSTRAINT FK_ADF3F3638DB60186 FOREIGN KEY (task_id) REFERENCES `task` (id)');
        $this->addSql('ALTER TABLE `task` ADD CONSTRAINT FK_527EDB25D5AA10AC FOREIGN KEY (robot_id) REFERENCES robot (id)');
    }

    public function down(Schema $schema) : void
    {
        // this down() migration is auto-generated, please modify it to your needs
        $this->addSql('ALTER TABLE `task` DROP FOREIGN KEY FK_527EDB25D5AA10AC');
        $this->addSql('ALTER TABLE data DROP FOREIGN KEY FK_ADF3F3638DB60186');
        $this->addSql('DROP TABLE data');
        $this->addSql('DROP TABLE robot');
        $this->addSql('DROP TABLE `task`');
    }
}
