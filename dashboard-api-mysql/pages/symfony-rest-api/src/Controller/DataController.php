<?php

namespace App\Controller;

use App\Entity\Data;
use App\Repository\TaskRepository;
use Doctrine\ORM\EntityManagerInterface;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Component\Serializer\SerializerInterface;

class DataController extends AbstractController
{
    /**
     * @Route("api/data", name="getdata", methods={"POST"})
     */
    public function index(Request $request, SerializerInterface $serializer, TaskRepository $task, EntityManagerInterface $em)
    {
        try{
            $post =$serializer ->deserialize($request -> getContent(), Data::class, 'json');

            $task = $task -> find(json_decode($request->getContent(),true)["task"]);
            $task -> setState("done");
            $post -> setTask($task);

            $em -> persist($task);
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
