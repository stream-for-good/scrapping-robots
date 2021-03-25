<?php

namespace App\Entity;

use App\Repository\TaskRepository;
use Doctrine\Common\Collections\ArrayCollection;
use Doctrine\Common\Collections\Collection;
use Doctrine\ORM\Mapping as ORM;

/**
 * @ORM\Entity(repositoryClass=TaskRepository::class)
 * @ORM\Table(name="`task`")
 */
class Task
{
    /**
     * @ORM\Id
     * @ORM\GeneratedValue
     * @ORM\Column(type="integer")
     */
    private $id;

    /**
     * @ORM\Column(name="`state`")
     */
    private $state;

    /**
     * @ORM\Column(name="`loop`")
     */
    private $loop;

    /**
     * @ORM\Column(type="datetime")
     */
    private $date;

    /**
     * @ORM\OneToMany(targetEntity=Data::class, mappedBy="task", orphanRemoval=true)
     */
    private $data;

    /**
     * @ORM\ManyToOne(targetEntity=Robot::class, inversedBy="task")
     * @ORM\JoinColumn(nullable=false)
     */
    private $robot;

    public function __construct()
    {
        $this->data = new ArrayCollection();
        $this->date = new \DateTime();
        $this->state = "pending";
    }

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getState(): ?string
    {
        return $this->state;
    }

    public function setState(string $state): self
    {
        $this->state = $state;

        return $this;
    }

    public function getLoop(): ?int
    {
        return $this->loop;
    }

    public function setLoop(int $loop): self
    {
        $this->loop = $loop;

        return $this;
    }

    public function getDate(): ?\DateTimeInterface
    {
        return $this->date;
    }

    private function setDefaultDate(){

    }
    public function setDate(\DateTimeInterface $date): self
    {
        $this->date = $date;

        return $this;
    }

    /**
     * @return Collection|Data[]
     */
    public function getData(): Collection
    {
        return $this->data;
    }

    public function addData(Data $data): self
    {
        if (!$this->data->contains($data)) {
            $this->data[] = $data;
            $data->setTask($this);
        }

        return $this;
    }

    public function removeData(Data $data): self
    {
        if ($this->data->removeElement($data)) {
            // set the owning side to null (unless already changed)
            if ($data->getTask() === $this) {
                $data->setTask(null);
            }
        }

        return $this;
    }

    public function getRobot(): ?Robot
    {
        return $this->robot;
    }

    public function setRobot(?Robot $robot): self
    {
        $this->robot = $robot;

        return $this;
    }

    public function __toString()
    {
        return ($this -> date )->format('Y-m-d H:i:s');
    }
}
