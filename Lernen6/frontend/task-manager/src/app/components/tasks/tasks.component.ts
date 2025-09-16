import { Component, OnInit } from '@angular/core';
import { Task, TaskService } from '../../services/task.service';

@Component({
    selector: 'app-tasks',
    templateUrl: './tasks.component.html',
    styleUrls: ['./tasks.component.css']
})
export class TasksComponent implements OnInit {
    tasks: Task[] = [];
    newTaskTitle: string = '';

    constructor(private taskService: TaskService) { }

    ngOnInit(): void {
        this.loadTasks();
    }

    loadTasks() {
        this.taskService.getTasks().subscribe(data => this.tasks = data);
    }

    addTask() {
        if (this.newTaskTitle.trim()) {
            this.taskService.addTask(this.newTaskTitle).subscribe(task => {
                this.tasks.push(task);
                this.newTaskTitle = '';
            });
        }
    }

    toggleTask(task: Task) {
        this.taskService.toggleTask(task.id, !task.completed).subscribe(updated => {
            task.completed = updated.completed;
        });
    }

    deleteTask(id: number) {
        this.taskService.deleteTask(id).subscribe(() => {
            this.tasks = this.tasks.filter(t => t.id !== id);
        });
    }
}
