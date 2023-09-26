using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyController : MonoBehaviour
{
    public UnityEngine.AI.NavMeshAgent agent;
    public Transform player;
    public LayerMask whatIsGround, whatIsPlayer;
    private Animator animator;
    public float health;

    //Patrolling
    public Vector3 walkPoint;
    public bool walkPointSet;
    public float walkPointRange;
    private float waitWalk;

    //Attacking
    public float timeBetweenAttacks;
    bool alreadyAttacked;

    //States
    public float sightRange, attackRange;
    public bool playerInSightRange, playerInAttackRange;

    private bool attacking;
    public bool dying = false; 

    private void Awake()
    {
        player = GameObject.Find("MaleCharacterPolyart").transform;
        agent = GetComponent<UnityEngine.AI.NavMeshAgent>();
        animator = GetComponent<Animator>();
    }

    private void Patrolling(){
        float waitWalk = Random.Range(20f,40f);
        animator.SetBool("Run", false);


        if (!walkPointSet) Invoke(nameof(SearchWalkPoint), 5f);
        if(walkPointSet) agent.SetDestination(walkPoint);

        Vector3 distanceToWalkPoint = transform.position - walkPoint;

        if(distanceToWalkPoint.magnitude < 1f) 
        {   
            //Debug.Log("Here");
            walkPointSet = false;
        }
    }

    private void ChasePlayer(){
        agent.SetDestination(player.position);
        animator.SetBool("Run", true);

    }
    private void AttackPlayer(){
        //make sure enemy doesn't move
        animator.SetBool("Run", false);
        agent.SetDestination(transform.position);

        transform.LookAt(player);

        if(!alreadyAttacked)
        {
            //Attack Code here
            attacking = true;
            animator.SetBool("Attack", true);
            alreadyAttacked = true;
            Invoke(nameof(ResetAttack), timeBetweenAttacks);
            }
    }

    void OnTriggerEnter(Collider other)
    {
        //Debug.Log("Collision");
        if (attacking == true)
        {
            attacking = false;
        
            Debug.Log("Attacking");
            if (other.tag == "Player")
            {
                AttributeManager attributeManager = other.GetComponent<AttributeManager>();
                if (attributeManager != null)
                {
                    other.GetComponent<AttributeManager>().TakeDamage(GetComponent<AttributeManager>().Strength);
                    Debug.Log("Slime did to "+ other.gameObject);
                    //attributeManager.DealDamage(gameObject);
                }
            }
        }  
    }

    private void ResetAttack()
    {
        alreadyAttacked = false;
    }

    private void ResetOneHit()
    {
        attacking = false;
        Invoke(nameof(ResetAttack), timeBetweenAttacks - GetAnimationDuration("Attack"));
    }

    private void SearchWalkPoint()
    {
        //Calculate random point in range
        float randomZ = Random.Range(-walkPointRange, walkPointRange);
        float randomX = Random.Range(-walkPointRange, walkPointRange);

        walkPoint = new Vector3(transform.position.x + randomX, transform.position.y, transform.position.z + randomZ);
        if(Physics.Raycast(walkPoint, -transform.up, 2f, whatIsGround))
        {
            walkPointSet = true;
        }
    }

    // Update is called once per frame
    void Update()
    {
        //Check for sight and attack range
        playerInSightRange = Physics.CheckSphere(transform.position, sightRange, whatIsPlayer);
        playerInAttackRange = Physics.CheckSphere(transform.position, attackRange, whatIsPlayer);

        if (!playerInSightRange&&!playerInAttackRange && !dying) Patrolling();
        if (playerInSightRange&&!playerInAttackRange && !dying) ChasePlayer();
        if (playerInSightRange&&playerInAttackRange && !dying) AttackPlayer();

        if (walkPointSet && !dying)
        {
            animator.SetBool("Walk", true);
        } else {
            animator.SetBool("Walk", false);
        }

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
