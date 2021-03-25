<?php

namespace App\Controller;

use App\Repository\TaskRepository;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\Routing\Annotation\Route;

class PendingTasksController extends AbstractController
{
    /**
     * @Route("api/pendingtasks", name="pending_tasks", methods={"GET"})
     */
    public function index(TaskRepository $task)
    {
        return $this->json($task -> getPendingTasks(),200, [], ['groups' => 'post:read']);
    }
}
