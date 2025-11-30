from kubernetes import client, config

def create_job(snippet_code: str):
    config.load_kube_config()
    batch_v1 = client.BatchV1Api()

    container = client.V1Container(
        name="runner",
        image="python:3.11-slim",
        command=["python", "/app/runner_entry.py"],
        resources=client.V1ResourceRequirements(
            limits={"memory": "300Mi", "cpu": "500m"}
        ),
        volume_mounts=[client.V1VolumeMount(mount_path="/workspace", name="workspace", read_only=False)],
        security_context=client.V1SecurityContext(
            allow_privilege_escalation=False,
            read_only_root_filesystem=True
        )
    )
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "code-runner"}),
        spec=client.V1PodSpec(
            containers=[container],
            restart_policy="Never",
            volumes=[client.V1Volume(name="workspace", empty_dir=client.V1EmptyDirVolumeSource())],
            security_context=client.V1PodSecurityContext(
                run_as_user=1000,
                run_as_group=1000,
                fs_group=1000,
                run_as_non_root=True
            ),
        ),
    )
    job_spec = client.V1JobSpec(template=template, backoff_limit=0)
    job = client.V1Job(
        api_version="batch/v1", kind="Job",
        metadata=client.V1ObjectMeta(name="code-runner-job"),
        spec=job_spec,
    )
    batch_v1.create_namespaced_job(body=job, namespace="default")