using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{

    private UnityEngine.AI.NavMeshAgent navMeshAgent;
    private Animator animator;
    public CharacterController controller;
    public float speed = 6f;
    public float turnSmoothTime = 0.1f;
    float turnSmoothVelocity;
    public Transform cam;
    private float attackSpeed = 1f;
    public bool canAttack = true;
    public bool oneHit = false;
    public bool attacking = false;
    public bool defending = false;

    public float GETY()
    {
        return transform.position.y;
    }
    // Start is called before the first frame update
    private void Awake()
        {
            navMeshAgent = GetComponent<UnityEngine.AI.NavMeshAgent>();
            animator = GetComponent<Animator>();
        }

    // Update is called once per frame

    public void Teleport(Vector3 position)
    {
        transform.position = position;
        Physics.SyncTransforms();
    }

    private void Update()
    {
        float horizontal = Input.GetAxisRaw("Horizontal");
        float vertical = Input.GetAxisRaw("Vertical");
        Vector3 direction = new Vector3(horizontal, 0f, vertical).normalized;

        if (direction.magnitude >= 0.05f)
        {
            float targetAngle = Mathf.Atan2(direction.x, direction.z) * Mathf.Rad2Deg + cam.eulerAngles.y;
            float angle = Mathf.SmoothDampAngle(transform.eulerAngles.y, targetAngle, ref turnSmoothVelocity, turnSmoothTime);
            transform.rotation = Quaternion.Euler(0f, angle, 0f);

            Vector3 moveDir = Quaternion.Euler(0f, targetAngle, 0f) * Vector3.forward;
            controller.Move(moveDir.normalized * speed * Time.deltaTime);
            animator.SetBool("Walk", true);

        } else {
            animator.SetBool("Walk", false);
        }

        if (Input.GetKeyDown("space"))
        {
            animator.SetTrigger("Jump");
        } 
        else if (Input.GetKeyDown("1") && canAttack)
        {
            attacking = true;
            animator.SetTrigger("Attack1");
            AnimationClip currentClip = animator.GetCurrentAnimatorClipInfo(0)[0].clip;
            canAttack = false;
            Invoke(nameof(resetHit),GetAnimationDuration(animator.GetCurrentAnimatorClipInfo(0)[0].clip.name));
        } 
        else if (Input.GetKeyDown("2") && canAttack)
        {
            attacking = true;
            animator.SetTrigger("Attack2");
            AnimationClip currentClip = animator.GetCurrentAnimatorClipInfo(0)[0].clip;
            canAttack = false;
            Invoke(nameof(resetHit),GetAnimationDuration(animator.GetCurrentAnimatorClipInfo(0)[0].clip.name));
        } 
        else if (Input.GetKeyDown("3") && canAttack)
        {
            attacking = true;
            animator.SetTrigger("Attack3");
            AnimationClip currentClip = animator.GetCurrentAnimatorClipInfo(0)[0].clip;
            canAttack = false;
            Invoke(nameof(resetHit),GetAnimationDuration(animator.GetCurrentAnimatorClipInfo(0)[0].clip.name));
        }
        else if (Input.GetKeyDown("4") && canAttack)
        {
            attacking = true;
            animator.SetTrigger("Attack4");
            AnimationClip currentClip = animator.GetCurrentAnimatorClipInfo(0)[0].clip;
            canAttack = false;
            Invoke(nameof(resetHit),GetAnimationDuration(animator.GetCurrentAnimatorClipInfo(0)[0].clip.name));
        }
        else if (Input.GetKeyDown("z"))
        {
            Debug.Log("Defend");
            animator.SetBool("Defend",true);
            defending = true;
        }
        animator.SetBool("Defend",false);
        defending = false;

    }

    private void Attack()
    {
        canAttack = true;
        oneHit = false;
    }

    private void resetHit()
    {
        Debug.Log("Resetting");
        attacking = false;
        Invoke(nameof(Attack),attackSpeed - GetAnimationDuration((animator.GetCurrentAnimatorClipInfo(0)[0].clip.name)));
    }

    private float GetAnimationDuration(string name)
    {
        if (animator == null)
        {
            Debug.LogError("Animator component is not assigned!");
            return 0f;
        }

        AnimatorClipInfo[] clips = animator.GetCurrentAnimatorClipInfo(0);
        foreach (AnimatorClipInfo clip in clips)
        {
            if (clip.clip.name.Equals(name))
            {
                return clip.clip.length;
            }
        }

        Debug.LogError("Animation clip with name '" + name + "' not found!");
        return 0f;
    }

}
