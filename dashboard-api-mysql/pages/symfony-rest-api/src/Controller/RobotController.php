<?php

namespace App\Controller;

use App\Entity\Robot;
use App\Repository\RobotRepository;
use Doctrine\ORM\EntityManagerInterface;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Component\Serializer\SerializerInterface;

class RobotController extends AbstractController
{
    /**
     * @Route("/api/setRobot", name="robot", methods={"POST"})
     */
    public function index(Request $request, SerializerInterface $serializer, RobotRepository $robot, EntityManagerInterface $em): Response
    {
        try{
            $post =$serializer ->deserialize($request -> getContent(), Robot::class, 'json');

            $em -> persist($post);
            $em -> persist($post);
            $em -> flush();
            return $this -> json([
                'status' => 201
            ]);
        } catch (\Exception $e) {
            return $this -> json([
                'status' => 400
            ]);
        }
    }
}
