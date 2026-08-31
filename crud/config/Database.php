<?php

class Database
{
    private static ?PDO $connection = null;

    public static function getConnection(): PDO
    {
        if (self::$connection === null) {

            $host = "localhost";
            $database = "loja";
            $username = "root";
            $password = "";

            $dsn = "mysql:host=$host;dbname=$database;charset=utf8mb4";

            self::$connection = new PDO(
                $dsn,
                $username,
                $password
            );

            self::$connection->setAttribute(
                PDO::ATTR_ERRMODE,
                PDO::ERRMODE_EXCEPTION
            );
        }

        return self::$connection;
    }
}

