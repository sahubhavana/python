sns.boxplot(
    data=df,
    x='Placement',
    y='CGPA',
    hue='Placement',
    palette='Set3',
    legend=False,
    ax=axes[1, 1]
)
axes[1, 1].set_title('CGPA by Placement Status')
axes[1, 1].set_xlabel('Placement')
axes[1, 1].set_ylabel('CGPA')

# Adjust spacing and display
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
